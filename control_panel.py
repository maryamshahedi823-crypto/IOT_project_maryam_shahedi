'''

 shahedi:hanoz kamel nist     


APM:
besiar awli , harj asoali dashtid dar haminja beporsid 
moafagh bashid

shahedi:salam vaght bekhyer khat 152 agh rahnamai konid mamnon mesham


'''

#===================================
#-----****-----------
#--------TASK  2, 3-----------------

class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'


    def turn_on(self):
        print('Done!!!')
        self.status='on'
        #--_.code ejra mishe

    def turn_off(self):
        print('off')
        self.status='off'
        #code ejra mishe 
       
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
        

class Sensor:
    
    def __init__(self,location,group,sensor_type,sensor_name):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
                
        
    def read_data(self):
        return 25




class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print(f'your device is added to {group_name}')
            
        else:
            print('your group is not exist') #...
        
        
        
        
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print('your group is not exist')
            
            
            
    def get_devices(self,group_name):
        devices=self.groups[group_name]
        return devices
        
        
        
    def trun_on_in_group(self,group_name):
        if group_name in self.groups
            devices=self.get_devices(group_name)
            for device in devices:
                device.turn_on()
            print(f'all devices have been successfully turned on in {group_name}')
        else:
            print('your group  is not exist') 
            
            
            
    def turn_off_in_group(self,group_name):
        
        if group_name in self.groups:
            devices=self.get_devices(group_name)
            for device in devices:
                device.turn_off()
         
             print(f'all devices have been successfully turned off in {group_name}') 
        else:
            print('your group  is not exist')
        
        
             
        pass
    
   
    
    def turn_on_all(self):
        if device in self.devices:#اگر دستگاه وجود داره در لیست دستگاهها
            for device in devices:
                device.turn_on()
            print('all devices have been successfully turned on')
        else:
            print('your devices  is not exist')
             
                
        
        
    
   def turn_off_all(self):
         if device in self.devices:#اگر دستگاه وجود داره در لیست دستگاهها
             for device in devices:
                 device.turn_off()
             print('all devices have been successfully turned off')
         else:
             print('your devices  is not exist')
               
             
    
    def get_status_in_group(self,group_name):
       if group_name in self.groups
        
              for device in devices:
         
                device.turn_on()  or   device.turn_off()
          
            
 
        
    def get_status_in_device_type(self,dvice_type):
        
        '''
        varaye kole devicd haee k hasan
        bere device_typeshono check kone
        
        fght lamparo bere check kone
        
        lamps -->lampa
        doors --L> fght doora
        (too ch groupi , device_type)
        
        statuseshono bede

        
        '''
        pass
    
    
    #tabe ee bename create_device???
    
    def create_sensor(self,group,sensor_type,sensor_name):
       if group in self.groups:
           location='home'
           new_sensor=sensor(location,group,sensor_type,sensor_name)
           self.sensor.append(new_sensor)
           print('your sensor is added to new_sensor')
       else:
           print('your group is not exist') #...
       
        
    
    def create_multiple_sensor(self,group,sensor_type,sensor_number):
        if group in self.groups:
              for i in range(1,sensor_number+1):
               se_name=f'{sensor_type}_{i}'
               self.create_sensor(group,sensor_type,se_name)

           print(f'{sensor_number} devices created!!')
        else:
           print('your group is not exist')
  
    
    
    
    
        
    



        
