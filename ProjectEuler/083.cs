// Problem 83

using System;
using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using System.IO;

namespace _083
{

    class Program
    {

        public static void Main(string[] args)
        {

            int[][] M = LoadMatrix("../files/83.txt");

            int s = Dijkstra(0, 0, 79, 79, M);

            Console.WriteLine(s);
            Console.ReadLine();

        }

        private static int[][] LoadMatrix(string path)
        {

            int[][] M = new int[80][];

            int i = 0;

            var lines = File.ReadLines(path);
            foreach (var line in lines)
            {

                string[] nums = line.Split(',');
                int[] row = new int[80];

                int j = 0;
                foreach (string num in nums) row[j++] = int.Parse(num);

                M[i++] = row;

            }

            return M;

        }

        private static int Dijkstra(int sx, int sy, int dx, int dy, int[][] M)
        {

            Dictionary<Point, Vertex> Q = new Dictionary<Point, Vertex>();

            for (int x = 0; x < M.Length; x++)
            {
                for (int y = 0; y < M.Length; y++)
                {
                    Vertex v = new Vertex(x, y);
                    Q.Add(v.p, v);
                }
            }

            Q[new Point(sx, sy)].dist = M[sy][sx];

            int min = Constants.infinity;

            Vertex u;
            ArrayList n;

            while (Q.Count != 0)
            {

                u = GetMin(Q);
                Q.Remove(u.p);

                n = GetNeighbours(Q, u);

                foreach (Vertex v in n)
                {

                    int alt = u.dist + M[v.p.Y][v.p.X];

                    if (alt < v.dist)
                    {
                        v.dist = alt;
                        v.prev = u;
                        if (v.p.X == dx && v.p.Y == dy && v.dist < min) min = v.dist;
                    }

                }

            }

            return min;

        }

        private static Vertex GetVertex(ArrayList Q, int x, int y)
        {

            foreach (Vertex v in Q)
            {
                if (v.p.X == x && v.p.Y == y) return v;
            }

            return null;

        }

        private static Vertex GetMin(Dictionary<Point, Vertex> Q)
        {

            Vertex minVertex = null;
            int minValue = Constants.infinity;

            foreach (KeyValuePair<Point, Vertex> v in Q)
            {
                if (v.Value.dist < minValue)
                {
                    minVertex = v.Value;
                    minValue = v.Value.dist;
                }
            }

            return minVertex;

        }

        private static ArrayList GetNeighbours(Dictionary<Point, Vertex> Q, Vertex u)
        {

            ArrayList ns = new ArrayList();

            if (u.p.X != 0 && Q.ContainsKey(new Point(u.p.X - 1, u.p.Y)))
                ns.Add(Q[new Point(u.p.X - 1, u.p.Y)]);
            if (u.p.X != 79 && Q.ContainsKey(new Point(u.p.X + 1, u.p.Y)))
                ns.Add(Q[new Point(u.p.X + 1, u.p.Y)]);
            if (u.p.Y != 0 && Q.ContainsKey(new Point(u.p.X, u.p.Y - 1)))
                ns.Add(Q[new Point(u.p.X, u.p.Y - 1)]);
            if (u.p.Y != 79 && Q.ContainsKey(new Point(u.p.X, u.p.Y + 1)))
                ns.Add(Q[new Point(u.p.X, u.p.Y + 1)]);

            return ns;

        }

    }

    class Vertex
    {

        public Point p;
        public int dist;
        public Vertex prev;

        public Vertex(int x, int y)
        {
            p = new Point(x, y);
            dist = Constants.infinity;
            prev = null;
        }

    }

    class Constants
    {
        public static int infinity = 9999999;
    }

}
