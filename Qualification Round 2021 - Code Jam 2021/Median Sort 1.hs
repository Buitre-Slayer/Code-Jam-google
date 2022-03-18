{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use head" #-}
import Control.Monad



main = do
    input <- getLine
    let inputList = map read $ words input :: [Int]
    let t = inputList !! 0
    let n = inputList !! 1
    let q = inputList !! 2
    forM_ [1 .. t] (\a -> do
        let combinations = [[i, j, k] | i <- [1 .. n], j <- [i + 1 .. n], k <- [j + 1 .. n]]
        let askQuestions a = (do
            putStrLn $ unwords $ map show a
            getLine
            )
        memorization <- forM combinations askQuestions
        print memorization
        return ()
        )
    