import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    tic = "QAN.AX"
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(
            tic=tic,
            pth=pth,
            start=start,
            end=end)
    df.to_csv(f"qan_prc_{year}.csv")

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)