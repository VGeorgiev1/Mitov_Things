class CreateManufactors < ActiveRecord::Migration[5.1]
  def change
    create_table :manufactors do |t|
      t.string :name
      t.string :location

      t.timestamps
    end
  end
end
