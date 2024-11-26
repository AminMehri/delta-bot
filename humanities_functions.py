import numpy as np


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - float(value))).argmin()
    return array[idx]


# 0
grades = [19.98,19.93,19.88,19.83,19.78,19.73,19.68,19.63,19.58,19.53,19.48,19.43,19.38,19.33,19.28,19.23,19.18,19.13,19.08,19.03,
		  18.95,18.85,18.75,18.65,18.55,18.45,18.35,18.25,18.15,18.05,
		  17.95,17.85,17.75,17.65,17.55,17.45,17.35,17.25,17.15,17.05,
		  16.95,16.85,16.75,16.65,16.55,16.45,16.35,16.25,16.15,16.05,
		  15.95,15.85,15.75,15.65,15.55,15.45,15.35,15.25,15.15,15.05,
		  14.88,14.63,14.37,14.12,13.88,13.63,13.37,13.12,12.88,12.63,12.37,12.12,11.88,11.63,11.37,11.12,
		  10.75,10.30,9,8,7,6
		  ]
taraz =  [12800, 12700, 12500, 12150, 11960, 11650, 11400, 11250, 11100, 11050, 11000, 10800, 10700, 10600, 10500, 10400, 10375, 10350, 10300, 10100, 9800, 9700, 9600, 9400, 9300, 9100, 9000, 8900, 8800, 8700, 8600, 8500, 8400, 8350, 8300, 8200, 8100, 8000, 7950, 7900, 7700, 7680, 7660, 7640, 7620, 7600, 7500, 7400, 7375, 7350, 7325, 7300, 7200, 7100, 7080, 7060, 7040, 7020, 7010, 7000, 6600, 6500, 6450, 6250, 6190, 6160, 6120, 5900, 5760, 5690, 5650, 5600, 5500, 5400, 5300, 5200, 5100, 5000, 4700, 4400, 4000, 4000]


def grade_taraz_func(grade:float):
    g = find_nearest(grades, value=grade)
    return taraz[grades.index(g)]


# 1
humanities_zarib = [8, 6, 2, 2, 5, 5, 5, 5]
# جامعه تاریخ فلسفه عربی اقتصاد روانشناسی ریاضی فنون
percents = {
10: [6900, 6900, 5600, 5600, 6300, 5900, 6250, 5850],
15: [7200, 7100, 6100, 6100, 6700, 6400, 6800, 6250],
20: [7600, 7500, 6600, 6600, 7100, 6750, 7200, 6700],
25: [8000, 8000, 7000, 7000, 7500, 7250, 7700, 7100],
30: [8300, 8300, 7400, 7400, 8000, 7600, 8100, 7550],
35: [8700, 8600, 7900, 7900, 8400, 8000, 8500, 7900],
40: [9100, 9000, 8200, 8200, 8750, 8550, 8850, 8300],
45: [9500, 9200, 8700, 8700, 8700, 8900, 9250, 8850],
50: [10200, 9700, 9100, 9100, 9200, 9500, 9700, 9200],
55: [10700, 10100, 9600, 9600, 9700, 9850, 10100, 9600],
60: [11000, 10500, 10250, 10250, 10300, 10350, 10550, 10100],
65: [11400, 11000, 10700, 10700, 10800, 10850, 11000, 10750],
70: [11700, 11600, 11100, 11100, 11100, 11250, 11400, 11200],
75: [12000, 11900, 11600, 11600, 11500, 11600, 11850, 11850],
80: [124000, 12350, 12000, 12000, 12100, 12100, 12300, 12300],
85: [128000, 12700, 12500, 12500, 12650, 12500, 12750, 12750],
90: [13200, 13100, 13100, 13100, 13100, 13000, 13150, 13100],
95: [13700, 13500, 13400, 13400, 13550, 13550, 13500, 13450],
100:[14100, 14000, 14000, 14000, 14000, 14000, 14000, 14000],
}

def percent_taraz(per:list):
    total_taraz = 0
    for ind, value in enumerate(per):
        g = find_nearest(list(percents.keys()), value=value)
        tara = percents.get(g)      
        total_taraz += tara[ind] * humanities_zarib[ind]
    return total_taraz / sum(humanities_zarib) # tot


# 2
taraz_kol = [12250, 11300, 11150, 10950, 10850, 10750, 10650, 10550, 10450, 10350, 10250, 10150, 10100, 
			 9900, 9800,9700,9600,9500,9400,9300,9200,9100,9000,8900,8800,8700,8600,8500,8400,8300,8200,
			 8100,8000,7900,7800,7700,7600,7500,7400,7300,7200,7100,7000,6900,6800,6700,6600,6500,6400,
			 6300,6200,6100,6000,5000]

keshvary_grade = ['1-100','100-200','200-300','300-400','400-500','500-600','600-700','700-800','800-900','900-1000','950-1040','1000-1200','1200-1400','1400-1600','1600-1800','1800-2000','2000-2200','2400-2600','2600-2800','3000-3200','3400-3600','400-4200','4600-4800','5000-5500','5500-6000','6500-7000','7000-7500','8000-8500','9000-9500','10000-10500','11000-12000','13000-13500','14500-15000','16000-16500','18000-18500','19000-20000','20000-22000','22000-24000','24000-26000','26000-31000','31000-34000','34000-37000','37000-41000','41000-45000','45000-47000','47000-52000','52000-56000','56000-62000','62000-68000','68000-72000','72000-78000','78000-79000','79000-8000','80000-81000','بالای 82000',]
mantaghe_1 = ['1-49', '50-95','96-140','141-183','141-183','184-225','226-266','245-262','267-305','306-343','343-416','417-486','487-552','553-616','617-678','679-737','738-795','795-906','907-960','960-1064','1064-1164','1164-1307','1307-1442','1442-1589','1590-1687','1687-1874','1875-1965','1965-2149','2149-2334','2334-2488','2488-2768','2768-3007','3007-3243','3243-3475','3475-3780','3780-4005','4005-4444','4444-4738','4738-5166','5166-5587','5587-6001','6001-6410','6410-6949','6949-7481','7481-7746','7746-8404','8404-8927','8927-9711','9711-10495','10495-11018','11018-11807','11018-11807','11807-12599','12599-13664','13664-15000',]
mantaghe_2 = ['1-39','40-74','75-109','109-188','120-165','189-223','223-258','230-256','259-293','294-327','327-397','397-466','466-535','535-604','604-672','672-741','741-810','810-946','946-1014','1014-1150','1150-1286','1286-1488','1488-1690','1690-1924','1924-2090','2090-2420','2420-2585','2585-2912','2912-3237','3237-3560','3560-4040','4040-4517','4517-4990','4990-5459','5459-6081','6081-6544','6544-7463','7463-8071','8071-8978','8978-9881','9881-10781','10781-11687','11687-12873','12873-14069','14069-14667','14667-16165','16165-17367','17367-19177','19177-20997','20997-22215','22215-24049','24049-25889','25889-28351','28351-30199','بالای 30000',]
mantaghe_3 = ['1-9','10-30','31-46','47-64','65-84','85-104','88-100','105-126','127-149','149-198','199-252','253-309','310-370','371-434','435-501','502-571','571-718','718-794','794-954','954-1120','1120-1379','1379-1648','1648-1971','1971-2207','2207-2687','2687-2930','2930-3421','3421-3917','3917-4419','4419-5177','5187-5978','5987-6839','6839-7613','7613-8662','8662-9459','9459-11077','11077-12171','12171-13830','13830-15508','15508-17199','17199-18900','18900-21178','21178-23461','23461-24604','24604-27459','27459-29738','29738-33144','33144-36534','36534-38784','38784-42146','42146-45495','45495-49946','49946-53279','53279-56000','بالای 56000',]

def taraz_kol_func(t_kol:float, mantaghe):
	g = find_nearest(taraz_kol, value=t_kol)
	result = f"رتبه کشوری: {keshvary_grade[taraz_kol.index(g)]}\n"
	if mantaghe == "1":
		result += f"رتبه منطقه یک: {mantaghe_1[taraz_kol.index(g)]}"

	elif mantaghe == "2":
		result += f"رتبه منطقه دو: {mantaghe_2[taraz_kol.index(g)]}"
	
	elif mantaghe == "3":
		result += f"رتبه منطقه سه: {mantaghe_3[taraz_kol.index(g)]}"	
	
	return result


# 3
import re

result_region_1 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300,
					 330, 360, 400, 430, 460, 500, 530, 560, 600, 640, 700, 750, 800, 850, 900, 950, 1000,
					   1075, 1150, 1250, 1350, 1450, 1600, 1800, 2000, 2250, 2500, 2750, 3000, 3400, 3800,
						 4200, 4800, 5200, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000,
						   12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 22000, 24000, 26000,
							 28000, 30000, 35000, 40000, 45000, 50000]

result_region_2 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300,
				    330, 360, 400, 430, 460, 500, 530, 560, 600, 640, 680, 700, 750, 800, 850, 900, 950, 1000,
					  1075, 1150, 1250, 1350, 1450, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200,
					    3400, 3600, 3800, 4000, 4400, 4800, 5200, 5600, 6000, 6500, 7000, 7500, 8000, 8500,
						  9000, 9500, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000,
						    20000, 22000, 24000, 26000, 28000, 30000, 33000, 36000, 40000, 45000, 50000]

result_region_3 = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 225, 250, 275, 300,
				    330, 360, 400, 430, 460, 500, 530, 560, 700, 750, 800, 850, 900, 950, 1000, 1075, 1150,
					  1250, 1350, 1450, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3300, 3600, 4000, 4400,
					    4800, 5200, 5600, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000, 12000,
						  13000, 14000, 15000, 16000, 18000, 19000, 20000, 22000, 24000, 26000, 28000, 30000,
						    33000, 36000, 40000, 45000, 50000]



def handle_resault(num: int, region: int):
	if region == 1:
		r_a = result_region_1.copy()
		f = find_nearest(r_a, value=num)
		r_a.remove(f)
		e = find_nearest(r_a, value=num)
		try:
			x = result_region_1[result_region_1.index(int(max(f,e))) + 1]
		except:
			return [f"{min(f, e)}تا{max(f, e)}", "END"]
	if region == 2:
		r_a = result_region_2.copy()
		f = find_nearest(r_a, value=num)
		r_a.remove(f)
		e = find_nearest(r_a, value=num)
		try:
			x = result_region_2[result_region_2.index(int(max(f,e))) + 1]
		except:
			return [f"{min(f, e)}تا{max(f, e)}", "END"]
	if region == 3:
		r_a = result_region_3.copy()
		f = find_nearest(r_a, value=num)
		r_a.remove(f)
		e = find_nearest(r_a, value=num)
		try:
			x = result_region_3[result_region_3.index(int(max(f,e))) + 1]
		except:
			return [f"{min(f, e)}تا{max(f, e)}", "END"]
	return [f"{min(f, e)}تا{max(f, e)}", f"{max(f, e)}تا{x}"]


def read_and_print_content(filename, start_pattern, end_pattern):
	with open(filename, 'r', encoding='windows 1256') as file:
		content = file.read()
			
	start_match = re.search(start_pattern, content)
	end_match = re.search(end_pattern, content)
	

	if start_match and end_match:
		start_index = start_match.end()
		end_index = end_match.start()
		return content[start_index:end_index]
	else:
		return f"اطلاعاتی برای این رتبه در دسترس نیست."

def get_konkor_grade(grade, region):
	if region == '1':
		filename = "file/humanities/منطقه 1.txt"
	elif region == '2':
		filename = "file/humanities/منطقه 2.txt"
	elif region == '3':
		filename = "file/humanities/منطقه 3.txt"
	else:
		return "خطایی رخ داده است"
	x = handle_resault(int(grade), int(region))
	print(x)
	start_pattern = x[0]
	end_pattern = x[1]
	return read_and_print_content(filename, start_pattern, end_pattern)

