# sheqmeni split()-is cloni

def split_clon(strings):
    result = [] #vqmnit cariel sias
    words = "" #vqmnit yvela sityvas cal calke aso aso
    for symbol in strings: #amdros mocemuli stringebis titoeul asoze movipovebt wvdomas
        if symbol == " ": #tu romelime simbolo udris cariels anu spaces
            result.append(words) #tu spacia eseigi sityva dasrulda da wordsshi rac aris vamatebt tavdapirvelad sheqminl listshi resulshi
            words="" #aq isev vabrunebt cariel cvlads rom sityva aiwyos axlidan
        else: #da ai tu arudris simbolo spaces mashin ukve chvens cariel cvladshi vamatebt am simbolos
            words += symbol #ai ak vamatebt simbolos cvladshi
    result.append(words) # es imitom rom bolo sityyvas xo speisi agar aakvs da amitom da magitom vamatebt bolo sityvas
    
    return result # aq ukve vabrunebt saboloo shedegs


print(split_clon('gaumarjos brat rogor xar'))