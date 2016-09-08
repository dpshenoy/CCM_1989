Module name:    CCM_1989.py
Author:         Dinesh Shenoy <astroshenoy@gmail.com>
Version:        Python 2.7
Purpose:        Computes interstellar extinction per Cardelli, Clayton
                & Mathis (CCM (1989)).
Uses:
    1.  Import into other scripts and use function ratio_A_lam_to_A_V()
    2.  Run as a program on its own with, e.g.
            $ ./CCM_1989.py 5.0     # for A_V = 5 mags visual extinction
Inputs:
    A_V     = magnitudes of visual extinction
Using this module responsibly requires reading/understanding CCM (1989).
When running this module as a free-standing program, if you want to generate
generate extinctions for specific wavelengths of your own choice, edit manually
below at "OPTIONAL MANUAL ADDITION".
