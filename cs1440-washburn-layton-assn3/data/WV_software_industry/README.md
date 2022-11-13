This data set can be generated from a full copy of the data file `../USA_full/2021.annual.singlefile.csv`.  Navigate to this directory in your shell and run these commands:

    head -n 1 ../USA_full/2021.annual.singlefile.csv > header.csv
    grep '^"54' ../USA_full/2021.annual.singlefile.csv > dat.csv
    grep '"5","5112"' dat.csv > trimmed.csv
    cat header.csv trimmed.csv > 2021.annual.singlefile.csv
    rm header.csv dat.csv trimmed.csv

*Note: You may use your own implementation of `tt.py` if it has been **installed**. See [Installing_Text_Tools.md](../../instructions/Installing_Text_Tools.md) for details and the modifications needed to the above sequence of commands.*

*Note: In some shell environments the above commands may be defined as _aliases_ with different default behaviors.  If you find that your data sets are generated incorrectly, try running each command prefixed with the `command` command modifier (try saying that 3 times fast!).  `command` supresses the effect of the alias for the duration of that command.  It looks like this:*

    command grep '^"${(P)STATE}' ../USA_full/$YEAR.annual.singlefile.csv > dat.csv