class Member < ApplicationRecord
	has_many :team_member_connections
	has_many :teams, through: :team_member_connections
	validates_format_of :email, :with => /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\Z/i, :on => :create
end
