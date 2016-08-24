#! /usr/bin/env python

'''
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
'''

import numpy as np ; import argparse

# This function takes in any wavelength and returns:
#   -- NaN if lam < 0.304   (lowest CCM goes is x = 3.3 --> lam = 0.303)
#   -- A_lam / A_V if 0.304 < lam < 3.44
#   -- 0.0 if lam > 3.45 (i.e., no extinction provided by this law)
def ratio_A_lam_to_A_V( lam ):

    import numpy as np
    R_V = 3.1   # Ratio of A_V to E(B-V) per CCM (1989)

    x = 1. / lam    # work in wavenumber

    # Wavelengths less than 0.30 micron
    if x > 3.3:
        return np.nan   # CCM 1989 doesn't go shorter than 0.303 micron

    # Wavelengths between 0.30 and 0.91 micron
    if x >= 1.1 and x <= 3.3:

        y = x - 1.82
        a = 1. + 0.17699*y - 0.50447*y**2 - 0.02427*y**3 + 0.72085*y**4 +\
                 0.01979*y**5 - 0.77530*y**6 + 0.32999*y**7
        b = 1.41338*y + 2.28305*y**2 + 1.07233*y**3 - 5.38434*y**4 -\
                 0.62251*y**5 + 5.30260*y**6 - 2.09002*y**7

        # Compute ratio A_lam / A_V per CCM (1989) Eq. (1).   This is
        # normalized by A_V, multiplying by A_V yields A_lam in magnitudes)
        normd_A_lam = a + b / R_V
        return normd_A_lam

    # Wavelengths between 0.91 and 3.45 micron
    if x >= 0.29 and x < 1.1:

        a =  0.574 * x**1.61
        b = -0.527 * x**1.61

        # Compute ratio A_lam / A_V per CCM (1989) Eq. (1).   This is
        # normalized by A_V, multiplying by A_V yields A_lam in magnitudes)
        normd_A_lam = a + b / R_V
        return normd_A_lam

    # Wavelengths beyond 3.45 micron (for longer lam, use other laws than CCM)
    if x < 0.29:

        return 0.0

# This function main() is for when this module is run as a program
def main():

    # Get user input of a value of A_V to use-- Note, this is just for the display
    # table, the choice of A_V has no effect on what is returned by the function
    # ratio_A_lam_to_A_V() above.
    parser = argparse.ArgumentParser()
    parser.add_argument( "A_V", type=float,
            help="# magnitudes of visual extinction to assume" )
    args = parser.parse_args()

    # OPTIONAL MANUAL ADDITION:
    # Designate any particular wavelengths (in terms of the equivalent x = 1 / lam
    # to two decimal places) that you want to appear in the table to be printed
    x_to_display = [ ]

    # these are the particular x values used in CCM 1989 Table 3
    x_table3 = [ 2.78, 2.27, 1.82, 1.43, 1.11, 0.80, 0.63, 0.46, 0.29 ]

    # concatenate and sort them to a single list in order of decreasing x
    x_picks = x_to_display + x_table3 ; x_picks.sort( reverse = True )

    # Reproduce the column in CCM's Table 3 labeled a(x) + b(x)/R_V, which is
    # A_lam / A_V, and also display A_lam itself in magnitudes
    print '\nR_V = 3.1 is fixed.'
    print 'For your choice of A_V = ', args.A_V, ':\n'
    print 'lam       x      A_lam/A_V       A_lam'
    print '(um)    (1/um)                   (mags)'
    print '----    ------   ---------       ------'

    for x in x_picks:
        normd_A_lam = ratio_A_lam_to_A_V( 1./x )
        print "%.2f \t %.2f \t %7.3f \t %.3f" % \
            ( 1./x, x, normd_A_lam, normd_A_lam * args.A_V )

# This allows running the module as a separe program; see also:
#   http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm
if __name__ == '__main__':
    main()
