#usr/bin/env python3

import geopandas as gpd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    world = gpd.read_file('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')

    world.plot(edgecolor='black', facecolor='none')
    plt.title('World Map')
    plt.show()
