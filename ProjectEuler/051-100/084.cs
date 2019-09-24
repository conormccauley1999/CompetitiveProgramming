using System;
using System.Collections.Generic;
using System.Linq;

class PE084 {

	public static void Main() {

		int[] timesVisited = new int[40];

		int position = 0;
		int conDubs = 0;

		Deck chestDeck = new Deck();
		Deck chanceDeck = new Deck();
		
		int turn = 0;
		while (turn < 1000000) {

			Random rand = new Random();
			int dieA = rand.Next(1, 5);
			int dieB = rand.Next(1, 5);

			if (dieA == dieB)
				conDubs++;
			else
				conDubs = 0;
			
			position += (dieA + dieB);
			position %= 40;

			if (conDubs == 3) {
				position = 10;
				conDubs = 0;
			}
			else if (position == 30) {
				position = 10;
			}
			else if (position == 2 || position == 17 || position == 33) {
				int chestCard = chestDeck.Next();
				if (chestCard == 1) position = 0;
				else if (chestCard == 2) position = 10;
			}
			else if (position == 7 || position == 22 || position == 36) {
				int chanceCard = chanceDeck.Next();
				if (chanceCard == 1) position = 0;
				else if (chanceCard == 2) position = 10;
				else if (chanceCard == 3) position = 11;
				else if (chanceCard == 4) position = 24;
				else if (chanceCard == 5) position = 39;
				else if (chanceCard == 6) position = 5;
				else if (chanceCard == 7 || chanceCard == 8) {
					if (position == 7) position = 15;
					if (position == 22) position = 25;
					if (position == 36) position = 5;
				}
				else if (chanceCard == 9) {
					if (position == 7) position = 12;
					if (position == 22) position = 28;
					if (position == 36) position = 12;
				}
				else if (chanceCard == 10) {
					if (position == 36) {
						int chestCard = chestDeck.Next();
						if (chestCard == 1) position = 0;
						else if (chestCard == 2) position = 10;
						else position -= 3;
					}
					else {
						position -= 3;
					}
				}
			}

			timesVisited[position]++;
			turn++;

		}

		List<KeyValuePair<int, int>> sorted = new List<KeyValuePair<int, int>>();
		
		for (int i = 0; i < 40; i++)
			sorted.Add(new KeyValuePair<int, int>(i, timesVisited[i]));

		sorted = sorted.OrderBy(x => x.Value).Reverse().ToList();
		Console.WriteLine($"{sorted[0]} {sorted[1]} {sorted[2]}");
		
	}

	class Deck {

		private int index = 0;
		private int[] cards = new int[] {
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
		};

		public Deck() {
			Shuffle();
		}

		public int Next() {
			if (index == 16) {
				Shuffle();
				index = 0;
			}
			return cards[index++];
		}

		private void Shuffle() {
			Random rand = new Random();
			cards = cards.OrderBy(x => rand.Next()).ToArray();    
		}

	}

}
