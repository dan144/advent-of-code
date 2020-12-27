module Main where

import Data.List

main :: IO ()
main = do
    contents <- readFile "input/5"
    print $ "PART ONE"
    print $ length . find_nice $ words contents
    print $ "PART TWO"

remove_sub sub s = filter (not . isInfixOf sub) s
remove_pairs strs = remove_sub "ab" $ remove_sub "cd" $ remove_sub "pq" $ remove_sub "xy" strs

is_vowel c = fromEnum $ c `elem` "aeiou"
vowel_count s = sum $ map is_vowel s
has_vowels strs = filter ((>=3) . vowel_count) strs

dupes s = map length $ group s
has_pair strs = filter ((>=2) . maximum . dupes) strs

find_nice strs = has_pair $ has_vowels $ remove_pairs strs
