#input

#ตัวแปร vriable เป็น identifier
#identifier เป็นชื่อที่ตั่งขึ้นมาเองต้องเป็นไปตามกฎของภาษา

std_name = input('ชื่ออะไรอะ : ')
std_id = input('รหัสนักศึกษา : ')
std_Y = input('ปีเกิด : ')
print('------------------------')
stdAge = 2023 - int(std_Y)
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
print(f"คุณเกิดปี {std_Y} อายุ {stdAge}")
print('------------------------')
#use ,
print('ยินดีต้อนรับ',str(std_id),'ชื่อ',str(std_name))
print('คุณเกิดปี',str(std_Y),'อายุ',str(stdAge))
#use +
print('ยินดีต้อนรับ'+' '+ str(std_id),'ชื่อ'+' '+ str(std_name))
print('คุณเกิดปี'+' '+ str(std_Y),'อายุ'+' '+ str(stdAge))
print('-------------------------')
#use เมธอด format
print('ยินดีต้อนรับ {0} ชื่อ {1}'.format(std_id,std_name))
print('คุณเกิดปี {0} อายุ {1}'.format(std_Y,stdAge))
print('-------------------------')
#use %
print('ยินดีต้อนรับ %s ชื่อ %s'%(std_id,std_name))
print('คุณเกิดปี %s อายุ %d'%(std_Y,stdAge))