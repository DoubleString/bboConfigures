function diffion()
    
    ion_int = textread('/home/jtao/work/work/rtk/2015325_test/ion_interp_FSGH');
    ion_ref = textread('/home/jtao/work/work/rtk/2015325_test/ion_refFSGH');
    
    trp_int = textread('/home/jtao/work/work/rtk/2015325_test/trp_interp_FSGH');
    trp_ref = textread('/home/jtao/work/work/rtk/2015325_test/trp_refFSGH');
    
    
    
    figure(4);
    plot(ion_int)
    ylim([-0.8,0.8]);
    figure(5);
    plot(ion_ref)
    ylim([-0.8,0.8]);
    
    %diffion = ion_int - ion_ref;
    
    for i = 1:size(ion_int,1)
        for j = 1:size(ion_int,2)
            diffion(i,j) = nan;
            
            if(ion_int(i,j) ~= nan && ion_ref(i,j)~= nan)
               diffion(i,j) = ion_int(i,j) - ion_ref(i,j); 
            end
        end
        
    end
        
        
    
    difftrp = trp_int - trp_ref;
    figure(1);
    plot(diffion);
    ylim([-0.15,0.15]);
    
    figure(2);
    plot(difftrp);
    ylim([-0.15,0.15]);
    
end

