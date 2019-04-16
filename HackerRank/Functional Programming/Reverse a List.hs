rev l = do
    let len = length l
    [l !! x | x <- [(len - 1), (len-2)..0]]
