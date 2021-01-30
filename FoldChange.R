library(tidyverse)
library(readxl)
# read files
ACPControl_Uniq_AA <- read_excel("C:/Users/ruchir/Desktop/30-289728564/UniqueSeq/result_files/PK03-control_7aaseqpercentcount.xlsx")
ACPR2_Uniq_AA <- read_excel("C:/Users/ruchir/Desktop/30-289728564/UniqueSeq/result_files/PK02-ROUND2_Unique_7aaSeqonly_percentcount.xlsx")

# If necessary convert the dataframe to tibble
as_tibble(ACPcontrol_Unique_AA2)
as_tibble(ACPR2_Unique_AA2)

# Join the files based on bio-panned R1 or R2 files with control(naive) file
ACPR2_C_Unique_AA <- left_join(ACPR2_Unique_AA2, ACPcontrol_Unique_AA2, by = "Peptide1")

# write the output in a new file
write_csv(ACPR2_C_Unique_AA, path = "C:/Users/ruchir/Desktop/30-289728564/UniqueSeq/result_files/ACPR2_C_Unique_AA.csv")

# replace NA value with percentage of a peptide having count = 1 in naive libraries percentage column
ACPR2_C_Unique_AA_updated <- ACPR2_C_Unique_AA %>% 
  mutate(Percentage.y = replace_na(Percentage.y,0.00003799126504834 ))

# write the output in a new file
write_csv(ACPR2_C_Unique_AA_updated, path = "C:/Users/ruchir/Desktop/30-289728564/UniqueSeq/result_files/ACPR2_C_Unique_AA_updated.csv" )

# calculate the log2 fold change. Percentage.x = calculated percentage of a peptide in R1 or R2. Percentage.y = calculated percentage of that peptide in control.
ACPR2_C_Unique_AA_log2updated <- ACPR2_C_Unique_AA_updated %>%
  mutate(log2foldchange = log2(Percentage.x/Percentage.y))

# write the output in a new file
write_csv(ACPR2_C_Unique_AA_log2updated, path = "C:/Users/ruchir/Desktop/30-289728564/UniqueSeq/result_files/ACPR2_C_Unique_AA_log2updated.csv")

# Filter the peptides with log2 fold change greater than equal to 5
ACPR2_log2foldchange2above <- filter(ACPR2_C_Unique_AA_log2updated,  log2foldchange >= 5)

# write the output in a new file. 
write_csv(ACPR2_log2foldchange5above, path = "C:/Users/ruchir/Desktop/30-289728564/UniqueSeq/result_files/ACPR2_log2foldchange2above.csv")