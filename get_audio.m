clc, clear, close all;
Fs=44100; %muestreo
Bt=16; %numero de bits
ch=1; %canal
obj=audiorecorder(Fs,Bt,ch,1);
%-------------------------------------
t=0;
disp('Presione una tecla para iniciar grabacion');
pause()
tic()
record(obj)
while t<3
    t=toc
end
stop(obj)
play(obj)
Datos1=getaudiodata(obj,'int16');
Datos2=double(Datos1);
Datos3=Datos2/max(Datos2);
figure,plot(Datos1)
figure,plot(Datos2)
figure,plot(Datos3)

Bin=abs(Datos3)>=0.2;
for i=1:length(Datos3)-441 %10ms de la se;al.
    f1(i)=mean(Bin(i:i+441));
end
figure,plot(Bin)
figure,plot(f1)
bin2 = f1>=0.1;
j=0;
for i=1:length(Datos3)-441
    if bin2(i)==1
        j=j+1;
        f2(j)=Datos3(i);
    end
end
figure,plot(f2)

corre=zeros(size(f2));
corre(2:end)=f2(1:end-1);
pre=corre-(0.95*f2);

for i=1:length(pre)
    if abs(pre(i))>=0.7
        pre(i)=0;
    end
end

contador=0;
frame=441;
overlap=44;
for i=1:overlap:length(pre)-(frame-1)
    contador=contador+1;
    imagen(:,contador)
end
w=windows(@hamming,441);
[fil, col]=size(imagen);
for i=1:contador
    imagen2(:,1)
end
for i=1:contador
    fft1=fft(imagen2(:,1));
    fft1=fft1(1:fil/2);
    FFT1(:,i)=abs(fft1);
end

comp1 = max(FFT1, [], 2);
comp2 = mean(FFT1, 2);
patron = (comp1 + comp2)/2;
