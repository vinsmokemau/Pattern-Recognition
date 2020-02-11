clc, clear, close all
senial1=? (cancion)
senial1=? (ruido)

target = senial1 + senial2
w1=rand(1,3);
b1=rand(1,3);
a=0.1;

for i=1:length(target)
	if i==1
		x=[senial2[i], 0, 0]';
	elseif i==2
		x=[senial2[i], senial2[i-1],0]';
	else
		x=[senial2[i], senial2[i-1],senial2[i-2]]
	end
	e = target[i] - y
	w1 = w1 + (a*e*x');
	b1 = b1 + (a*e);
end