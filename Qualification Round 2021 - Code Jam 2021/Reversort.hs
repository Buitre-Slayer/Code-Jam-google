import Control.Monad


findMin [] = 0
findMin [x] = x
findMin (x:xs) =
    if nextMin < x then nextMin else x
    where nextMin = findMin xs




findPos _ [] = 1
findPos _ [x] = 1
findPos s (x:xs) =
    if s == x then 1 else 1 + findPos s xs



solution [] = 0
solution [x] = 0
solution x =
    pos + solution(tail (reverse (take pos x)) ++ reverse (take (length x - pos) (reverse x)))
    where pos = findPos (findMin x) x



main = do
    nTests <- getLine
    forM_ [1..read nTests :: Int] (\a ->do
        n <- getLine
        valuesImpure <- getLine
        let values = map read $ words valuesImpure :: [Int]
        putStrLn("Case #" ++ show a ++ ": " ++ show(solution values))
        return ()
        )
    