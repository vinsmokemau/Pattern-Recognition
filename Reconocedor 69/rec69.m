clc, clear all, close all;

I6=imread('entrena6.bmp');
I9=imread('entrena9.bmp');
I9=imresize(I9, size(I6));
figure(1)
imshow([I6 I9], []) %Con el corchete vacio busca el numero mas bajo y lo trata como negro
[L6, n6]=bwlabel(I6, 8);
[L9, n9]=bwlabel(I9, 8);

figure(2)
imshow([L6 L9], [])

for j=1:2
    if(j==1)
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
        [i, n];
        y=zeros(size(L));
        ii=find(L==1);
        y(ii)=1;
        %[ii, jj]=find(L==1);
        y1=imfill(y, 'holes');
        y2=xor(y,y1);
        [ii, jj]=find(L==1);
        h1=max(ii);
        h2=max(ii);
        [ii, jj]=find(y2==1);
        h=mean(ii)-h2;
        z(i)=h/(h1-h2);
    end
    
    if(j==1)
        z6=z;
    else
        z9=z;
    end

end

figure(3)
clf
hist(z6)
hold on
hist(z9)
th=(mean(z6)+mean(z9))/2
plot([th, th], [0, 35], 'g' )

disp('Parte2: Prueba(presionar enter)')
pause
close all

J=imread('prueba69.bmp');
%J=imdilate(J, ones(3,3));
[N M]=size(J);
figure(1)
imshow(J, [])
hold on