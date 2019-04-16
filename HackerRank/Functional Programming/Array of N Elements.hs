fn n =
    [x | x <- [1..n]]

main = do
    n <- readLn :: IO Int
    print (fn(n))
