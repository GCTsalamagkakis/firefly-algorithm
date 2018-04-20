import random
import math

programs = []

class trainingProgram:
	
	def __init__(self, intensity, volume, recovery, caloricNeeds):
		self.intensity = intensity
		self.volume = volume
		self.recovery = recovery
		self.caloricNeeds = caloricNeeds
		#h parakatw sunarthsh einai mia tuxaia sunarthsh pou upoti8etai oti deixnei poios einai o katalhlos sunduasmos twn metavlhtwn
		self.brightness = ((math.cos(2*intensity)-math.sin(3*volume))*math.e**recovery)/caloricNeeds
		
	def Adaptation(self):
		#oi metavlhtes change upologizoun poso 8a allaksei h antistoixh metavlhth tou program pou einai sto parakatw loop
		intensityChange = 0
		volumeChange = 0
		recoveryChange = 0
		caloricNeedsChange = 0
		count = 0
		#testing values
		print("before mutation")
		print(self.intensity)
		print(self.volume)
		print(self.recovery)
		print(self.caloricNeeds)
		print("after mutation")
		#for each program in our global list
		for candidateProgram in programs:
			if candidateProgram != self:
				if candidateProgram.brightness > self.brightness:

					#oi metavlhtes difference apo8hkeuoun th diafora se ka8e metavlhth anamesa sto programma pou elegxoume kai ta programmata me megalutero brightness
					intensityDifference = candidateProgram.intensity - self.intensity
					volumeDifference = candidateProgram.volume - self.volume
					recoveryDifference = candidateProgram.recovery - self.recovery
					caloricNeedsDifference = candidateProgram.caloricNeeds - self.caloricNeeds
					#upologizw thn apostash ws ton meso oro diaforas twn metavlhtwn
					#to +1 ston diaireth einai gia na mh ginei diairesh me to 0
					distance = (abs(intensityDifference) + abs(volumeDifference) + abs(recoveryDifference) + abs(caloricNeedsDifference))/4
					relativeBrightness = candidateProgram.brightness/(abs(distance)+1)
					
					if relativeBrightness > self.brightness:
						#metraw apo posa programmata exei ephreastei to programa pou einai sto loop kai enhmerwnw gia tis allages pou prepei na ginoun
						count+=1
						intensityChange += intensityDifference/(distance+1)
						volumeChange += volumeDifference/(distance+1)
						recoveryChange += recoveryDifference/(distance+1)
						caloricNeedsChange += caloricNeedsDifference/(distance+1)
		
		#random uniform gia to tuxaio mutation pou prepei na ginei gia na mh kolhsei se topiko elaxisto/megisto to programa
		self.intensity += intensityChange/(2*count+1) + random.uniform(-0.4,0.4)
		self.volume += volumeChange/(2*count+1) + random.uniform(-0.4,0.4)
		self.recovery += recoveryChange/(2*count+1) + random.uniform(-0.4,0.4)
		self.caloricNeeds += caloricNeedsChange/(2*count+1) + random.uniform(-0.4,0.4)
		
		#elegxos gia na mh vgei tipota out of bounds
		if self.intensity > 10:
			self.intensity = 10
		if self.volume > 10:
			self.volume = 10
		if self.recovery > 10:
			self.recovery = 10
		if self.caloricNeeds > 10:
			self.caloricNeeds = 10
			
		if self.intensity < 0:
			self.intensity = 0
		if self.volume < 0:
			self.volume = 0
		if self.recovery < 0:
			self.recovery = 0
		if self.caloricNeeds < 0:
			self.caloricNeeds = 0
		print(self.intensity)
		print(self.volume)
		print(self.recovery)
		print(self.caloricNeeds)
		print("self.brightness: " + str(self.brightness))
		print("next chromosome")

#200 tuxaia xrwmoswmata mpenoun sth global list
for i in range(200):
	
	intensity = random.uniform(0,10)
	volume = random.uniform(0,10)
	recovery = random.uniform(0,10)
	caloricNeeds = random.uniform(0,10)
	
	programs.append(trainingProgram(intensity, volume, recovery, caloricNeeds))
	
#o algorithmos trexei gia 1000 generations kai meta vriskei to megisto brightness kai emfanizei ta stoixeia toy
for i in range(1000):
	
	for candidateProgram in programs:		
		candidateProgram.Adaptation()
maximum = programs[0].brightness
for candidateProgram in programs:
	if candidateProgram.brightness > maximum:
		maximum = candidateProgram.brightness
		maxIntensity = candidateProgram.intensity
		maxVolume = candidateProgram.volume
		maxRecovery = candidateProgram.recovery
		maxCaloricNeeds = candidateProgram.caloricNeeds

print("best")
print("inensity: " + str(maxIntensity))
print("volume: " + str(maxVolume))
print("recovery: " + str(maxRecovery))
print("caloric needs: " + str(maxCaloricNeeds))
print("brightness: " + str(maximum))