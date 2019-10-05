l = [2,3,4,5]

print(sum(l))
if sum(years_sum_count_F[names_years_count_female[name][i][0]]) is exit
    for name in names_years_count_male:
    for i in range(len(names_years_count_male[name])):
        if sum(years_sum_count_M[names_years_count_male[name][i][0]]) != 0:    
            for first_name,male_first_year,min_male_frequency in sorted([(name,names_years_count_male[name][i][0],int(names_years_count_male[name][i][1])/sum(years_sum_count_M[names_years_count_male[name][i][0]]))],key = g , reverse = True)[0]:
                if not female_first_year:
                    print(f'In all years, {first_name} was never given as a male name.')
                else:
                    print(f'In terms of frequency, {first_name} was the most popular '
                          f'as a male name first in the year {male_first_year}.\n'
                          f'  It then accounted for {min_male_frequency:.2f}% of all female names.'
                          )
else:
    print(f'In all years, {first_name} was never given as a male name.')