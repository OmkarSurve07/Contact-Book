cars = [audi, audi, audi, BMW, jaguar, jaguar]
final_car_count = {}
for car in cars:
    if car not in final_car_count:
        final_car_count.update({car:1})
    else:
        final_car_count.update({car:final_car_count[car]+1})
print(final_car_count)