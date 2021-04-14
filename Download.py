import os
import time
os.chdir("C:\\Users\Admin\Documents\Workspace\GFZ\ERA5")

start = time.perf_counter()

import cdsapi

pressure_list = ['500', '750', '1000']

for i in pressure_list:
    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': 'specific_humidity',
            'pressure_level': i,
            'year': [
                '2011', '2012', '2013',
                '2014', '2016', '2017',
                '2018', '2019', '2020',
                '2021',
            ],
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
            'area': [
                38, 23, 37,
                24,
            ],
        },
        'specific_hum_'+ i + '.nc')

end = time.perf_counter()
