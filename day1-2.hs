module Main where

import Data.List
import Data.List.Split

main :: IO ()
main = do
    print $ "Run a daily module, dayN"

day1 = do
    contents <- readFile "input/1"

    print $ "PART ONE"
    print $ sum $ map converter contents
    print $ "PART TWO"
    print $ find_basement contents

find_basement contents = length $ takeWhile (/= (-1)) $ scanl (+) 0 $ map converter contents
converter '(' = 1
converter ')' = -1
converter _ = 0

day2 = do
    contents <- readFile "input/2"
    print $ sum $ map wrapping_paper $ splitOn "\n" contents
    print $ sum $ map ribbon $ splitOn "\n" contents

get_size [a,b,c] = 3*a*b + 2*a*c + 2*b*c
get_size _ = 0
get_ribbon [a,b,c] = 2*(a+b) + a*b*c
get_ribbon _ = 0
wrapping_paper contents = get_size $ sort $ map stoi $ splitOn "x" contents
ribbon contents = get_ribbon $ sort $ map stoi $ splitOn "x" contents
stoi s = read s ::Int
