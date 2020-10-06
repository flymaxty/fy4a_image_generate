#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, glob

from satpy.scene import Scene

def main():
    proxy = 'http://10.211.55.2:7000'

    os.environ['http_proxy'] = proxy 
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy

    # 加载FY4A文件
    filenames = glob.glob('/home/ye/Documents/20201004/FY4A-_AGRI--_N_REGC_1047E_L1-_FDI-_MULT_NOM_20201004043418_20201004043835_4000M_V0001.HDF')
    print(filenames)

    scn = Scene(filenames, reader='agri_l1')
    print(scn.available_dataset_names())

    # scn.load(['C02'])
    # scn.show('C01')
    # scn.save_dataset('C02', filename='{sensor}_{name}.png')
   
    print(scn.available_composite_names())

    composite = 'true_color'
    scn.load([composite])
    print(scn['true_color'].attrs['area'].area_id)
    print(scn['true_color'].attrs['start_time'])
    # scn.show(composite)
    scn.save_dataset(composite, filename='{platform_name}_{sensor}_{resolution}_{name}.png')


if __name__ == "__main__":
    main()