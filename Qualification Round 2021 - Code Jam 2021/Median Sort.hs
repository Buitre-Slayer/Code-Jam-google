{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use head" #-}
import Control.Monad
import Data.List

ask [a, b, c] = do
    putStrLn $ show a ++ " " ++ show b ++ " " ++ show c
    r <- getLine
    return (read r :: Int)

initialize x = [l !! 0, x, l !! 1]
    where
        l = delete x [1, 2, 3]

solve [x, y] _ = []
solve (x:y:z:xs) s  
    | ask [x, y, z] == y = solve ([y, z] ++ xs) s
    let hn = 1 
        
    

main = do
    input <- getLine
    let inputList = map read $ words input :: [Int]
    let t = inputList !! 0
    let n = inputList !! 1
    let q = inputList !! 2
    forM_ [1 .. t] (\a -> do
        firstQuestion <- ask [1, 2, 3]
        let l = initialize firstQuestion
        
        getLine
        )