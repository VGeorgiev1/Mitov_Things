class ManufactorsController < ApplicationController
  before_action :set_manufactor, only: [:show, :edit, :update, :destroy]

  # GET /manufactors
  # GET /manufactors.json
  def index
    @manufactors = Manufactor.all
  end

  # GET /manufactors/1
  # GET /manufactors/1.json
  def show
  end

  # GET /manufactors/new
  def new
    @manufactor = Manufactor.new
  end

  # GET /manufactors/1/edit
  def edit
  end

  # POST /manufactors
  # POST /manufactors.json
  def create
    @manufactor = Manufactor.new(manufactor_params)

    respond_to do |format|
      if @manufactor.save
        format.html { redirect_to @manufactor, notice: 'Manufactor was successfully created.' }
        format.json { render :show, status: :created, location: @manufactor }
      else
        format.html { render :new }
        format.json { render json: @manufactor.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /manufactors/1
  # PATCH/PUT /manufactors/1.json
  def update
    respond_to do |format|
      if @manufactor.update(manufactor_params)
        format.html { redirect_to @manufactor, notice: 'Manufactor was successfully updated.' }
        format.json { render :show, status: :ok, location: @manufactor }
      else
        format.html { render :edit }
        format.json { render json: @manufactor.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /manufactors/1
  # DELETE /manufactors/1.json
  def destroy
    @manufactor.destroy
    respond_to do |format|
      format.html { redirect_to manufactors_url, notice: 'Manufactor was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_manufactor
      @manufactor = Manufactor.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def manufactor_params
      params.require(:manufactor).permit(:name, :location)
    end
end
