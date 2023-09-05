
city_list = ["Karaj","Tehran","Esfahan","Mashhad","Rasht","Shiraz"] 
population_list = [300000, 1000000, 3800000, 500000, 1900000, 100000] 
area_list = [100, 200, 500, 150, 300, 100] 

km2_to_ha = lambda x:x*100
calculate_density = lambda x,y:int(x/km2_to_ha(y))

result_dict = {i:calculate_density(j,k) for i,j,k in zip(city_list,population_list,area_list)}

[print(f'{key}: {value}') for key,value in result_dict.items()]
print('-------------------')
print('High Density Cities:')
[print(f'{key}: {value}') for key,value in result_dict.items() if value>=50]