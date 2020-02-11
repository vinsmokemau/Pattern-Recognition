function salida = cargar_imagen()
    
    persistent carga;
    persistent w;
    
    if (isempty(carga))
        base=zeros(120000,24);
        for personas=1:4
            cd(strcat('s', num2str(personas)))
            for fotos=1:6
                a=imread(strcat('F', num2str(fotos),'.bmp'));
                base(:,(fotos-1)*4+personas)=a(:);
                %base(:,(fotos-1)*4+personas)=reshape(a,size(a,1)*size(a,2),1);
            end
            cd ..
        end
        w=unit8(base);
    end
    carga=1;
    salida=w;
end

