import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

files = [file for file in os.listdir('.') if os.path.isfile(file)]

for file in files:
    split_filename = file.split("_")
    if len(split_filename) == 5:

        # Get important info
        utdate = split_filename[0]
        target = split_filename[1]
        method = split_filename[2]

        # Plot
        df = pd.read_csv(file)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_yscale('log')
        df['contrast'] *= 5
        df['sep'] *= 0.009942
        ax.plot(df['sep'], df['contrast'])
        plt.xlabel("Angular Separation (arcsec)")
        plt.ylabel("5 sigma contrast")
        title_str = "Optimal Contrast Curve for %s (%s)" % (target, method.upper())
        plt.title(title_str)

        # Save image under ..\static\slow\utdate\target\opt_cc\utdate_target_method.png
        dir = "../static/slow/%s/%s/opt_cc" % (utdate.replace("-",""), target)
        if not os.path.exists(dir):
            os.makedirs(dir)

        plt.savefig('%s/%s_%s_%s.png' % (dir, utdate, target, method))
