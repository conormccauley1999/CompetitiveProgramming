len :: [a] -> Int
len lst = do
	sum [1 | _ <- lst]
