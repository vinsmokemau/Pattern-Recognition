clc, clear, close all;

senales = load('AudioCorazon.txt')

for i=1:6
    senal1 = senales(:,i);

    sound(senal1, 2000);

    % figure, spectrogram(senal1,220,20)

    A = spectrogram(senal1,220,20);

    B = sum(real(A'));

    figure, plot(B)
end