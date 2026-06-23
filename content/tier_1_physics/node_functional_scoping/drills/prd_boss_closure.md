# PRD: Stateful Cost Tracker
## Overview
A Closure is a nested function that remembers variables from its outer enclosing scope even after the outer function has returned. This lets us build lightweight, stateful tracking engines without writing a formal Class.
## Requirements
1. Write a factory function make_cost_tracker() that returns a closure.
2. Each time the returned function is called with a token count, it accumulates the tokens.
3. It must return the running total cost in dollars (at a rate of $0.000002 per token).
