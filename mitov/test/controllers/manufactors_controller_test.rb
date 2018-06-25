require 'test_helper'

class ManufactorsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @manufactor = manufactors(:one)
  end

  test "should get index" do
    get manufactors_url
    assert_response :success
  end

  test "should get new" do
    get new_manufactor_url
    assert_response :success
  end

  test "should create manufactor" do
    assert_difference('Manufactor.count') do
      post manufactors_url, params: { manufactor: { location: @manufactor.location, name: @manufactor.name } }
    end

    assert_redirected_to manufactor_url(Manufactor.last)
  end

  test "should show manufactor" do
    get manufactor_url(@manufactor)
    assert_response :success
  end

  test "should get edit" do
    get edit_manufactor_url(@manufactor)
    assert_response :success
  end

  test "should update manufactor" do
    patch manufactor_url(@manufactor), params: { manufactor: { location: @manufactor.location, name: @manufactor.name } }
    assert_redirected_to manufactor_url(@manufactor)
  end

  test "should destroy manufactor" do
    assert_difference('Manufactor.count', -1) do
      delete manufactor_url(@manufactor)
    end

    assert_redirected_to manufactors_url
  end
end
