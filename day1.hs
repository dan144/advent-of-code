module Main where

import Data.List
import Data.List.Split

main :: IO ()
main = do
    contents <- readFile "input/1"
    print $ "PART ONE"
    print $ sum $ map converter contents
    print $ "PART TWO"
    print $ find_basement contents

find_basement contents = length $ takeWhile (/= (-1)) $ scanl (+) 0 $ map converter contents
converter '(' = 1
converter ')' = -1
converter _ = 0
