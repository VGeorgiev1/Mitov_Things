class Car < ApplicationRecord
	belongs_to :manufactor
	validate do
		if self.model != "red" && self.model != "green" && self.model != "blue"
			errors.add(:model, "Only red greeen and blue cars allowed!")			
		end
	end
	validate do
		if Manufactor.find(self.manufactor_id).cars.select{ |c| c.date.year == self.date.year && c.model == self.model}.count == 3
			errors.add(:cars, "Too many cars with that color for this year!")
		end
	end
end


