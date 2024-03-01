GLASSTONE//UNLEASHED-nuclear weapons effects modelling in Python
=====================================================

## FAQ

## Huh? What is this?

This is a fork of a nuclear blast effects library developed by Edward Geist. The link to the actual master repo will be linked below.

If you care about accuracy/stability at all, use the official project.

## Why does this exist?

The purpose of this fork is to expand on the original data by extrapolating values that previously returned an error. The innacuracy rate is higher, but can give you (limited) insight
into situations and calculations that were not possible by solely relying on the original dataset.

**Example: you for whatever reason wanted to know the ground radiation dose of a 500 megaton warhead detonated in LEO. Or maybe the overpressure of a 90 kiloton warhead detonated
just a few meters away. This kind of ridiculous speculation is only possible with extrapolation.**

Perhaps the development of some simple CLI interface for easily calculating/graphing results could be worked in after the codebase refactoring is finished.

## Can I help?

YES. What I need is for the program to be stress tested in any way possible; a lot of the modified modules tie into each other and break occassionally when a random parameter/variable is exceeded.

Also, if anyone has access to **LEGALLY OBTAINED/SHARABLE** nuclear weapon blast datasets not present in the original repo, let me know and I'll do my best to integrate it.

## Is the project finished?

Nope, not even close. Check back to this section for updates on progress.

| TODO://                                           |                                                                                                                                                |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| overpressure.py                                 | remove error checking code, integrate extrapolation algorithm                                                                                  
| thermal.py                                    | remove error checking code, integrate extrapolation algorithm                                          
| radiation.py                                    | remove error checking code, integrate extrapolation algorithm                                          


## Links/Liscense

**Master Repository**

https://github.com/GOFAI/glasstone

**UNLEASHED Repository**

https://github.com/SharpClaw007/glasstoneUNLEASHED

License: MIT
