import argparse

from neup_zld.core.zld_sweep_1param import run_1d_sensitivity
from neup_zld.core.zld_sweep_2param import run_2d_sensitivity
# from neup_zld.core.zld_sweep_3param import run_3d_sensitivity  # I don't think this code works right now, only has a function named "run_2d_sensitivity"


def run_sweep(num_params: int, species: list = ["Li"], verbose: bool = False):

    if num_params == 1:
        run_1d_sensitivity()
    elif num_params == 2:
        run_2d_sensitivity()
    # elif num_params == 3: 
    #     run_3d_sensitivity()


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Run the optimization.")
    p.add_argument("num_params", help="How many parameters to run a sweep over")
    p.add_argument("species", type=list, default=["Li"], help="which mineral species will be included in the simulation")
    p.add_argument("-v", "--verbose", action="store_true", help="Stream solver log")
    return p.parse_args(argv)


if __name__ == "__main__":
    args = parse_args()
    run_sweep(num_params=args.num_params, species=args.species, verbose=args.verbose)
