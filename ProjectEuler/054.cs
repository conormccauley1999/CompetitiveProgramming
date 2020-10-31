// Problem 54

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace PokerHands
{

    class Program
    {

        static void Main(string[] args)
        {

            int handsWon = GetHandsWon();
            Console.WriteLine(handsWon);
            Console.ReadLine();

        }

        static int GetHandsWon()
        {

            int handsWon = 0;

            var stream = new FileStream("../files/54.txt", FileMode.Open, FileAccess.Read, FileShare.ReadWrite);
            var file = new StreamReader(stream, Encoding.UTF8, true, 128);
            int x = 1;
            String line;
            while ((line = file.ReadLine()) != null)
            {

                bool winnerWasPlayerOne = false;

                String[] rawCards = line.Split(' ');

                Hand handOne = new Hand(rawCards.Take(5).ToArray());
                Hand handTwo = new Hand(rawCards.Skip(5).ToArray());

                int handOneValue = handOne.GetValue();
                int handTwoValue = handTwo.GetValue();

                if (handOneValue > handTwoValue)
                {
                    handsWon++;
                    winnerWasPlayerOne = true;
                }

                else if (handOneValue == handTwoValue) {

                    int[] handOneHighCards = handOne.GetHighCards();
                    int[] handTwoHighCards = handTwo.GetHighCards();

                    int highCardCount = handOneHighCards.Length;

                    for (int i = 0; i <= highCardCount; i++)
                    {

                        if (handOneHighCards[i] > handTwoHighCards[i])
                        {
                            handsWon++;
                            winnerWasPlayerOne = true;
                            break;
                        }

                        else if (handOneHighCards[i] < handTwoHighCards[i])
                        {
                            break;
                        }

                    }

                }
                
                Console.WriteLine("Hand #{0} - Winner {1}", x, (winnerWasPlayerOne) ? "P1" : "P2");
                x++;

            }

            return handsWon;

        }
        
    }

    public class Hand
    {

        private int value;
        private int[] highCards;

        private Card[] cards;
        private int[] sortedFaces;
        private Dictionary<int, int> cardCounts;

        public Hand(String[] cards)
        {

            this.cards = new Card[5];

            for (int i = 0; i < 5; i++)
            {
                this.cards[i] = new Card(cards[i]);
            }

            sortedFaces = GetSortedFaces();
            cardCounts = GetCardCounts();

            value = CalcValue();

        }

        public int GetValue()
        {
            return value;
        }

        public int[] GetHighCards()
        {
            return highCards;
        }

        private int CalcValue()
        {

            int value = (
                IsRoyalFlush() ? 9 :
                IsStraightFlush() ? 8 :
                IsFourOfAKind() ? 7 :
                IsFullHouse() ? 6 :
                IsFlush() ? 5 :
                IsStraight() ? 4 :
                IsThreeOfAKind() ? 3 :
                IsTwoPairs() ? 2 :
                IsPair() ? 1 :
                0
            );

            if (value == 0)
            {
                highCards = sortedFaces;
                Array.Reverse(highCards);
            }

            return value;

        }

        private int[] GetSortedFaces()
        {

            int[] sortedFaces = new int[5];

            for (int i = 0; i <= 4; i++)
            {
                sortedFaces[i] = cards[i].GetFace();
            }

            Array.Sort(sortedFaces);

            return sortedFaces;

        }

        private Dictionary<int, int> GetCardCounts()
        {

            cardCounts = new Dictionary<int, int>();

            foreach (Card card in cards)
            {

                int face = card.GetFace();

                if (cardCounts.ContainsKey(face)) { cardCounts[face]++; }
                else { cardCounts.Add(face, 1); }

            }

            cardCounts.OrderByDescending(x => x.Value);

            return cardCounts;
            
        }

        private bool IsRoyalFlush()
        {

            bool result = IsStraightFlush() && (sortedFaces[4] == 14);

            if (result)
            {
                highCards = new int[0];
            }

            return result;

        }

        private bool IsStraightFlush()
        {

            bool result = IsFlush() && IsStraight();

            if (result)
            {
                highCards = new int[] { sortedFaces[4] };
            }

            return result;

        }

        private bool IsFourOfAKind()
        {

            bool result = false;
            int[] tempHighCards = new int[2];

            foreach (KeyValuePair<int, int> cardCount in cardCounts)
            {

                if (cardCount.Value == 4)
                {
                    tempHighCards[0] = cardCount.Key;
                    result = true;
                }

                else if (cardCount.Value == 1)
                {
                    tempHighCards[1] = cardCount.Key;
                }

            }

            return result;

        }

        private bool IsFullHouse()
        {

            bool hasThree = false;
            bool hasPair = false;
            int[] tempHighCards = new int[2];

            foreach (KeyValuePair<int, int> cardCount in cardCounts)
            {

                if (cardCount.Value == 3)
                {
                    tempHighCards[0] = cardCount.Key;
                    hasThree = true;
                }

                else if (cardCount.Value == 2)
                {
                    tempHighCards[1] = cardCount.Key;
                    hasPair = true;
                }

            }

            bool result = (hasPair && hasThree);

            if (result)
            {
                highCards = tempHighCards;
            }

            return result;

        }

        private bool IsFlush()
        {

            bool result = (
                (cards[0].GetSuit() == cards[1].GetSuit()) &&
                (cards[1].GetSuit() == cards[2].GetSuit()) &&
                (cards[2].GetSuit() == cards[3].GetSuit()) &&
                (cards[3].GetSuit() == cards[4].GetSuit())
            );

            if (result)
            {
                highCards = sortedFaces;
                Array.Reverse(highCards);
            }

            return result;

        }

        private bool IsStraight()
        {

            bool result = (
                (sortedFaces[0] == (sortedFaces[1] - 1)) &&
                (sortedFaces[1] == (sortedFaces[2] - 1)) &&
                (sortedFaces[2] == (sortedFaces[3] - 1)) &&
                (sortedFaces[3] == (sortedFaces[4] - 1))
            );

            if (result)
            {
                highCards = new int[] { sortedFaces[4] };
            }

            return result;

        }

        private bool IsThreeOfAKind()
        {

            bool result = false;
            int[] tempHighCards = new int[3];
            List<int> values = new List<int>();

            foreach (KeyValuePair<int, int> cardCount in cardCounts)
            {

                if (cardCount.Value == 3)
                {
                    tempHighCards[0] = cardCount.Key;
                    result = true;
                }

                else if (cardCount.Value == 1)
                {
                    values.Add(cardCount.Key);
                }

            }

            if (result)
            {
                values.Sort();
                tempHighCards[1] = values.ElementAt(1);
                tempHighCards[2] = values.ElementAt(0);
                highCards = tempHighCards;
            }

            return result;

        }

        private bool IsTwoPairs()
        {

            bool result = false;
            int[] tempHighCards = new int[3];
            List<int> values = new List<int>();

            int pairs = 0;

            foreach (KeyValuePair<int, int> cardCount in cardCounts)
            {

                if (cardCount.Value == 2)
                {
                    pairs++;
                    values.Add(cardCount.Key);
                }

                else if (cardCount.Value == 1)
                {
                    tempHighCards[2] = cardCount.Key;
                }

            }

            result = (pairs == 2);

            if (result)
            {
                values.Sort();
                tempHighCards[0] = values.ElementAt(1);
                tempHighCards[1] = values.ElementAt(0);
                highCards = tempHighCards;
            }

            return result;

        }

        private bool IsPair()
        {

            bool result = false;
            int[] tempHighCards = new int[4];
            List<int> values = new List<int>();

            foreach (KeyValuePair<int, int> cardCount in cardCounts)
            {

                if (cardCount.Value == 2)
                {
                    result = true;
                    tempHighCards[0] = cardCount.Key;
                }

                else
                {
                    values.Add(cardCount.Key);
                }

            }

            if (result)
            {
                values.Sort();
                tempHighCards[1] = values.ElementAt(2);
                tempHighCards[2] = values.ElementAt(1);
                tempHighCards[3] = values.ElementAt(0);
                highCards = tempHighCards;
            }

            return result;

        }

    }

    public class Card
    {

        private int face;
        private int suit;

        public Card(String card)
        {

            String rawFace = card[0].ToString();
            String rawSuit = card[1].ToString();

            face =
                (rawFace == "A") ? 14 :
                (rawFace == "K") ? 13 :
                (rawFace == "Q") ? 12 :
                (rawFace == "J") ? 11 :
                (rawFace == "T") ? 10 :
                int.Parse(rawFace)
            ;

            suit =
                (rawSuit == "H") ? 3 :
                (rawSuit == "D") ? 2 :
                (rawSuit == "C") ? 1 :
                0
            ;

        }

        public int GetFace()
        {
            return face;
        }

        public int GetSuit()
        {
            return suit;
        }

    }

}
