# This is a list of multiple acquisitions for specific targets. 
# In some cases new acquisitions need to be added from the catalogue.
prs_img_list = \
    {  
    # ID : [description, tstart, tend, central_lat, central_lon]
    '5039': ['Po_river_01', '20200418101719', '20200418101723', 45.0041, 10.9567],
    '30245': ['Po_river_02', '20220616102037', '20220616102041', 45.1633, 10.792],
    '9409': ['Po_river_03', '20211027101743', '20211027101747', 45.1599, 10.7733],
    '23623': ['Po_river_04', '20220407101408', '20220407101413', 45.165, 10.7921],
    'L_01': ['L_Po_river_01', '2021-10-28-00', '00_2021-10-28-23', 45.3116, 10.5682],
    'L_02': ['L_Po_river_02', '2022-06-16-00', '00_2022-06-16-23', 45.3116, 10.5682]
    }


use_cases= \
    {  
    
    #this dictionary reports coregistration and CD parameters for each use case composed of two acquisitions of the previous list. Different AOI or coregistration and CD parameters can be set for the same pair of acquisitions, so there can be multiple entries for the same couple of images.

    # ID : [[parameters_acquisition_1, parameters_acquisition_2], [AOI_coreg_topleft_x , AOI_coreg_topleft_y , AOI_coreg_bottomright_x , AOI_coreg_bottomright_y] , [AOI_cd_topleft_x , AOI_cd_topleft_y , AOI_cd_bottomright_x , AOI_cd_bottomright_y],CD_threshold,[iterations_coreg_number,[radius_coreg_1,riadius_coreg_2],rank_coreg,pyramid_coreg_levels],[bandcva_x,bandcva_y],single_difference_band]
    
    'Po_01': [[prs_img_list['9409'],prs_img_list['30245']],[None,None,None,None],'g',[490,605],80,[8,[70,70],4,5],[560,730],760],
    'Po_02': [[prs_img_list['9409'],prs_img_list['23623']],[None,None,None,None],'g',[550,600],90,[8,[70,70],4,5],[560,730],760], #[200,150] 550,600
    'Land_Po_01': [[prs_img_list['L_01'],prs_img_list['L_02']],[None,None,None,None],'g',[850,1009],80,[8,[70,70],4,5],[1610,2200],760] #[700,0] 850,1009
    }