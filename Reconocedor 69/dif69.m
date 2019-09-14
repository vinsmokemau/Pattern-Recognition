clc, clear all, close all
I6=imread('entrena6.bmp');
I9=imread('entrena9.bmp');
I9=imresize(I9, size(I6));
figure(1)
imshow([I6 I9],[]); %concatena matrices, con [] busca el valor mas bajo y lo
%considera negro y busca el valor mas alto y lo considera blanco
[L6,n6]=bwlabel(I6,8);
[L9,n9]=bwlabel(I9,8);
figure(2)
imshow([L6 L9],[]);
%------------------------------------------------------
%ENTRENAMIENTO
%------------------------------------------------------
for j=1:2
    if (j==1)
        L=L6;
        n=n6;
        disp('procesando el numero 6')
    else
        L=L9;
        n=n9;
        disp('procesando el numero 9')
    end
    z=zeros(n,1);
    for i=1:n
        [i,n]; %sirve para saber e que objeto estoy del total de los que procesare
        y=zeros(size(L));
        ii=find(L==i);
        y(ii)=1;
        %[ii,jj]=find(L==i);
        y1=imfill(y,'holes');
        y2=xor(y,y1);
        [ii,jj]=find(L==i);
        h1=max(ii);
        h2=min(ii);
        [ii,jj]=find(y2==1);
        h=mean(ii)-h2;
        z(i)=h/(h1-h2);
    end
    if(j==1)
        z6=z;
    else
        z9=z;
    end
end
     
        %y 6
        %y1 6 relleno
        %y2 solo el relleno
        %h1 num max de filas
        %h2 min de filAS
%-----------------------------------------------------------
%pruebas
%------------------------------------------------------------
figure(3)
clf
hist(z6)
hold on
hist(z9)
th=(mean(z6)+mean(z9))/2;
plot([th,th],[0,35],'g')

disp('Parte 2: prueba(presionar enter)')
pause
close all

Test=imread('entrena9.bmp');
%Test=imdilate(Test,ones(3,3));
[N,M]=size(Test);
figure(1), hold on,
imshow(Test,[])
hold on

[L, n]=bwlabel(Test, 8);
n6=0;
n9=0;

for i=1:n
    [i n];
    y=zeros(size(L));
    ii=find(L==i);
    y(ii)=1;
    [ii, jj]=find(L==i);
    R=L(min(ii):max(ii), min(jj):max(jj));
    xx=[min(jj) min(jj) max(jj) max(jj) min(jj)];
    yy=[min(ii) max(ii) max(ii) min(ii) min(ii)];
    y1=imfill(y, 'holes');
    y2=xor(y,y1);
    h1=max(ii);
    h2=min(jj);
    [ii, jj]=find(y2==1);
    h=mean(ii)-h2;
    z=h/(h1-h2);
    figure(2)
    imshow(R)
    if z > th
        title('seis')
        color='r';
        n6=n6+1;
    else
        title('nueve')
        color='g';
        n9=n9+1;
    end
    figure(1)
    plot(xx,yy,color)
    pause(2)
end

verdadero6=input('cuantos 6 fueron clasificados correctamente?');
verdadero9=input('cuantos 9 fueron clasificados correctamente?');

falso6=verdadero6-n6;
falso9=verdadero9-n9;

MC=[verdadero6 falso6
    falso9 verdadero9]
porcentaje=(verdadero6+verdadero9)/(n6+n9);
