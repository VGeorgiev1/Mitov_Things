class TeamMemberConnection < ApplicationRecord
	belongs_to :team
	belongs_to :member
	validate do
		if Member.find(self.member.id).teams.select{|t| t.color == Team.find(self.team_id).color}.count >= 1
			errors.add(:team_member_connections, "Already in a team wit that color")
		end
	end
end
