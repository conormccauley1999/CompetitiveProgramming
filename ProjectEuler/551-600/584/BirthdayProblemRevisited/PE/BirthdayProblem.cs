using System;
using System.Collections.Generic;

namespace PE
{

    class BirthdayProblem
    {

        private const int EV_MAX = 12;
        private static Dictionary<TreeConfig, double> cache = new Dictionary<TreeConfig, double>();

        public static void Main(string[] args)
        {

            /*PTree tree = new PTree(4, 2, 3, 30);
            Console.WriteLine(tree.Calculate());
            Console.WriteLine(tree.ToString());*/
            
            //Console.WriteLine(E(3, 1, 10)); // expect 5.78688636
            //Console.WriteLine(E(3, 7, 100)); // expect 8.48967364
            Console.WriteLine(E(4, 7, 365));

            Console.ReadLine();

        }

        private static double E(int n, int k, int d)
        {

            double v = 0;

            for (int m = 2; m <= EV_MAX; m++)
                v += m * P(m, n, k, d);
            
            return v;

        }

        private static double P(int m, int n, int k, int d)
        {

            double v = 1.0;

            for (int i = 2; i < m; i++)
                v *= (1 - GetPTreeValue(i, n, k, d));

            return v * GetPTreeValue(m, n, k, d);

        }

        private static double GetPTreeValue(int m, int n, int k, int d)
        {

            TreeConfig config = new TreeConfig(m, n, k, d);

            if (cache.ContainsKey(config)) return cache[config];
            else
            {
                double value = (new PTree(m, n, k, d)).Calculate();
                cache[config] = value;
                return value;
            }
            
        }

        private struct TreeConfig
        {

            int m, n, k, d;

            public TreeConfig(int m, int n, int k, int d)
            {
                this.m = m;
                this.n = n;
                this.k = k;
                this.d = d;
            }

        }

        class PTree
        {

            public static int maxDepth;
            public static int maxWidth;
            public static int minSuccesses;

            private int m, n, k, d;
            private Node root;

            public PTree(int m, int n, int k, int d)
            {

                this.m = m;
                this.n = n;
                this.k = k;
                this.d = d;

                maxDepth = m;
                maxWidth = k + 1;
                minSuccesses = n;

                root = new Node(1, 1, d, d, 1);
                root.GenerateChildren();

            }

            public double Calculate()
            {
                return root.Calculate();
            }

            public override string ToString()
            {

                string result = $"{root.ToString()}\n";

                List<Node> nodesInPrevLayer = new List<Node>();
                nodesInPrevLayer.Add(root);

                for (int i = 2; i <= maxDepth; i++)
                {

                    string layerString = "";

                    List<Node> nodesInLayer = new List<Node>();
                    foreach (Node node in nodesInPrevLayer)
                        nodesInLayer.AddRange(node.children);

                    foreach (Node node in nodesInLayer)
                        layerString += $"{node.ToString()} ";

                    result += $"{layerString}\n";
                    nodesInPrevLayer = nodesInLayer;

                }
                
                return result;

            }

            class Node
            {

                private int depth;
                private int width;
                private int numerator;
                private int denominator;
                private int successes;

                public List<Node> children;

                public Node(int depth, int width, int numerator, int denominator, int successes)
                {

                    this.depth = depth;
                    this.width = width;
                    this.numerator = numerator;
                    this.denominator = denominator;
                    this.successes = successes;

                    children = new List<Node>();

                }

                public void GenerateChildren()
                {

                    int failNumerator = denominator;

                    if (width == maxWidth)
                    {
                        children.Add(new Node((depth + 1), width, width, denominator, successes + 1));
                        failNumerator -= width;
                    }
                    else
                    {
                        for (int i = width; i <= maxWidth; i++)
                        {
                            children.Add(new Node((depth + 1), i, ((i == 1) ? 1 : 2), denominator, successes + 1));
                            failNumerator -= ((i == 1) ? 1 : 2);
                        }
                    }

                    children.Add(new Node((depth + 1), width, failNumerator, denominator, successes));
                    
                    if ((depth + 1) == maxDepth) return;

                    foreach (Node child in children)
                        child.GenerateChildren();

                }

                public double Calculate()
                {

                    double value = numerator / (double) denominator;

                    double sum = 0;
                    foreach (Node child in children)
                        sum += child.Calculate();

                    return (successes < minSuccesses && depth == maxDepth) ? 0 : (value * ((children.Count == 0) ? 1 : sum));

                }

                public override string ToString()
                {
                    return $"({successes})";
                }

            }

        }

        /*class PTree
		{

			public static int maxDepth;
			public static int maxWidth;

			private int n, k, d;
			private Node root;

			public PTree(int n, int k, int d)
			{
				this.n = n;
				this.k = k;
				this.d = d;
			}

			public void Generate()
			{
				maxDepth = n;
				maxWidth = k + 1;
				root = new Node(1, 1, d, d);
				root.GenerateChildren();
			}

			public double Calculate()
			{
				return root.Calculate();
			}

			class Node
			{

				private int depth;
				private int width;
				private int numerator;
				private int denominator;

				private List<Node> children;

				public Node(int depth, int width, int numerator, int denominator)
				{
					this.depth = depth;
					this.width = width;
					this.numerator = numerator;
					this.denominator = denominator;
					children = new List<Node>();
				}

				public void GenerateChildren()
				{

					if (width == maxWidth)
						children.Add(new Node((depth + 1), width, width, denominator));
					else
						for (int i = width; i <= maxWidth; i++)
							children.Add(new Node((depth + 1), i, ((i == 1) ? 1 : 2), denominator));

					if ((depth + 1) == maxDepth) return;

					foreach (Node child in children)
						child.GenerateChildren();

				}

				public double Calculate()
				{

					double value = numerator / (double) denominator;

					double sum = 0;
					foreach (Node child in children)
						sum += child.Calculate();
					
					return value * ((children.Count == 0) ? 1 : sum);
					
				}

			}

		}*/

    }

}
