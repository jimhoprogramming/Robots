%   get the image at onetime one image   
%
%
clear all;

A=imread('data\road2.jpg');

%    trans to gray imag

I=rgb2gray(A);

%   mxn meam wave filtering 
%
%m=10;
%n=10;
%%I=meanFilter(m,n,I);
%K=fspecial('average',m,n);
%II=uint8(fix(filter2(K,I)));

%   use gusi mean filter
%sigma=1
%K=fspecial('gaussian',[10 10],sigma);
%II=uint8(fix(filter2(K,I)));


%   besider detection
II=edge(I,'sobel');




%        show result
%figure 1 ; 
%imshow(I);
figure 2;
imshow(II);
