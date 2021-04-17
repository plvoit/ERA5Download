import os
import time
import cdsapi
os.chdir("C:\\Users\Admin\Documents\Workspace\GFZ\ERA5")

start = time.perf_counter()

station_coords = [ [38, 23, 37, 24, ],  # ATH
                  [41, 44, 40, 45],  # NANM
                  [44, 76, 43, 77],  # AATB
                  [47, 7, 46, 8],  # JUNG
                  [69, -134, 68, -133],  # INVK
                  [57, -62, 56, -61],  # NAIN
                  [77, -69, 76, -68],  # THUL
                  [-89, -1, -90, 1] #SOPO
                  ]

station_names = ['AATB', 'NANM', 'JUNG', 'INVK', 'NAIN', 'THUL', 'SOPO'] # NANM und ATHEN fehlt, weil schon fast alles runtergeladen wurde
pressure_list = ['100', '250', '500', '750', '1000']
variable_list = ['specific_humidity', 'relative_humidity', 'temperature']

# format 'grib'?
for k in range(len(station_names)):
    for j in variable_list:
        for i in pressure_list:
            c = cdsapi.Client()

            c.retrieve(
                'reanalysis-era5-pressure-levels',
                {
                    'product_type': 'reanalysis',
                    'format': 'netcdf',
                    'variable': j,
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
                    'area': station_coords[k]

                },
                station_names[k] + '_' + j + '_' + i + '.nc')

end = time.perf_counter()
