f :: [Int] -> [Int]
f lst =
    [lst !! x | x <- [0..(length lst)], odd x]

main = do
	inputdata <- getContents
	mapM_ (putStrLn. show). f. map read. lines $ inputdata
