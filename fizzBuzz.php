<?php

class Solution
{
    function fizzBuzz($n)
    {
        $answer = array();
        for ($i = 1; $i <= $n; $i++) {
            $fizzBuzz = "";
            if ($i % 3 == 0) {
                $fizzBuzz .= "Fizz";
            }
            if ($i % 5 == 0) {
                $fizzBuzz .= "Buzz";
            }
            $answer[$i] = ($fizzBuzz === "") ? strval($i) : $fizzBuzz;
        }
        return $answer;
    }
}
