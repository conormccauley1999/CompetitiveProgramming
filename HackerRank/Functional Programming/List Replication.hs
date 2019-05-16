f :: Int -> [Int] -> [Int]
f n arr =
    concatMap (replicate n) arr

main :: IO ()
main = getContents >>=
       mapM_ print. (\(n:arr) -> f n arr). map read. words
