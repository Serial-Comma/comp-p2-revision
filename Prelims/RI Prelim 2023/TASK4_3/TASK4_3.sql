SELECT COUNT(*), Gender, ROUND(AVG(AGE),1), ROUND(AVG(Weight)),ROUND(AVG(Height))
from(SELECT FitnessRecord.MemberID, Age, Height, Weight, MAX(WorkoutDate), Gender 
FROM FitnessRecord, Member
WHERE FitnessRecord.MemberID=Member.MemberID
GROUP BY Member.MemberID)
GROUP BY Gender