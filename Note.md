# 通用语法
## Statements
### Group Statements 
**Syntax:**

    group_name ( name ) {
      ... statements ...
    }


### Attributes Statements
- Simple Attributes 
- Complex Attributes

#### Simple Attributes 
**Syntax:**

    attribute_name : attribute_value ;

#### Complex Attributes
**Syntax:**

    attribute_name (parameter1, [parameter2, parameter3 ...] );

### Define Statements
**Syntax:**

    define (attribute_name, group_name, attribute_type ) ;

### include\_file 语句
可用于减小文件大小。例如：

    cell() {
      area : 0.1 ;
      ...
      include_file (memory_file) ;
      ...
    }

使用限制：

- 不能循环调用，`include_file`调用的文件中不允许存在`include_file`语句；
- 一个`inlcude_file`命令只能调用一个文件；
- `include_file`命令不能替代`group_value`/`attribute_value`语句；
- `include_file`不能替代边界或跨边界存在；

## Library Groups
    library ( my_library ) {
      ...
    }
### 通用属性
- `technology`
- `delay_model`
- `bus_naming_style`

#### technology attribute
**Syntax:**

    technology (name) ;

#### delay\_model attribute
**Syntax:**

    delay_model : value ;

#### bus\_nameing\_style attribute
**Syntax:**

    bus_naming_style : "string";

### Delay and Slew Attributes
- `input_threshold_pct_fall`
- `input_threshold_pct_rise`
- `output_threshold_pct_fall`
- `output_threshold_pct_rise`
- `slew_derate_from_library`
- `slew_lower_threshold_pct_fall`
- `slew_lower_threshold_pct_rise`
- `slew_upper_threshold_pct_fall`
- `slew_upper_threshold_pct_rise`

### Definint Unit
- `time_unit` : 1ps / 10ps / 100ps / 1ns
- `voltage_unit` : 1mV / 10mV / 100mV / 1V
- `current_unit` : 1uA / 10uA / 100uA / 1mA / 10mA / 100mA / 1A
- `pulling_resistance_unit` : 1ohm / 10ohm / 100ohm / 1kohm 
- `capacitive_load_unit` : `capacitive_load_unit (value, unit)` - unit : ff / pf
- `leakage_power_unit` : 1W / 100mW / 10mW / 1mW / 100uW / 10uW / 1uW / 100nW / 10nW / 1nW / 100pW / 10pW / 1pW

# Building Environments
全局默认设置在library层次，可以在别处被覆盖。

## 单元的默认设置
- `default_cell_leakage_power` : value ;

## 端口的默认设置
- `default_inout_pin_cap` : value ;
- `default_input_pin_cap` : value ;
- `default_output_pin_cap` : value ;
- `default_max_fanout` : value ;
- `default_max_transition` : value ;
- `default_fanout_load` : value ;

## 线负载的默认设置
- `default_wire_load` : `wire_load_name ;`
- `default_wire_load_capacitance` : `wire_load_name ;`
- `default_wire_load_resistance` : `wire_load_name ;`
- `default_wire_load_area` : `wire_load_name ;`

## 其他环境设置
- `default_operating_conditions` : `operating_condition_name`;
- `default_connection_class` : name1 [name2 name3 ...];

# 定义operating condition
**Synatx:**
	library ( lib_name ) {
	  operating_conditions ( name ) {
	    ... operating conditions description ...
	  }
	}

- `name` : operating condition名字，库文件中唯一
- `process` : 工艺厂生产中scaling系数，0-100的浮点数，大多数为1.0
- `process_label` : "name" ; 
- `temperature` : value ;
- `voltage` : value ;
- `tree_type` : model ;
  - 定义环境互连模型
  - model是下述三种模型中的一种:
    - `best_case_tree` : 负载端口物理上紧邻驱动。此种模型下，不存在引线线电容和电阻；
    - `balanced_tree` : 负载端口分散在互连线的相等分支上。此种模型下，每一个负载端口分摊占线电容和电阻总量相等分量的电容和电阻；
    - `worst_case_tree` : 负载端口在物理互连线最远端。此种模型下，每一个负载端口均承担全部的线电容和线电阻；

# 定义Power Supply Cells
使用`power_supply` group建模multiple power supply cells

**Syntax:**
    power_supply () {
      default_power_rail : string ;
      power_rail (string, float) ;
      power_rail (string, float) ;
      ...
    }

**Example:**
    power_supply () {
      default_power_rail : VDD0 ;
      power_rail (VDD1, 5.0) ;
      power_rail (VDD2, 3.3) ;
      ...
    }

# 定义Wire Load Groups
使用`wire_load` group 和`wire_load_selectioin` group来为不同尺寸的电路指定`capacitance`系数、`resistance`系数、`area`系数、`slope`和`fanout_length`。

## wire\_load group
**Syntax:**
    wire_load ( name ) {
      resistance : value ;
      capacitance : value ;
      area : value ;
      slope : value ;
      fanout_length(fanout, length, \
                    average_capacitance, standard_deviation, \
                    number_of_nets ) ;
    }

- `resistance` : value ; 
浮点数，指定单位长度引线的线电阻
- `capacitance` : value ;
浮点数，指定单位长度引线的线电容
- `area` : value ;
浮点数，指定单位长度引线面积
- `slope` : value ;
浮点数，指定斜率。用来刻画超出`fanout_length`最长长度之后fanout长度的行为。

`wire_load` group 可以指定下述两个负载属性：
- `fantou_lenth ( fanout, length, average_capacitance, standard_deviation, number_of_nets ) ;`
  当人为指定`fanout_length`时，只指定fanout和length两个参数。
- `interconect_delay ( template_name ) { values(float, ...float, ...float, ...float,...) ; }`
  为线延迟定义查找表和值。可以再values之前overwrite默认的index值。

## wire\_load\_table group
`wire_load_table` : 更灵活的方式准确估算互连延迟。
**Syntax:**
    wire_load_table(name) {
      fanout_length(fanout, length);
      fanout_capacitance(fanout, capacitance);
      fanout_resistance(fanout, resistance);
      fanout_area(fanout, area);
    }

- `name` : string
- `fanout` : int
- `length`, `capacitance`, `resistance`, `area` : float

## wire\_load\_selection group

# 指定延迟比例属性
- 在library层次定义的k因子作用于整个库；
- 用户可以为单个指定的cell指定operating conditions来覆盖library层次的值；

## 端口和引线电容因子
以下`multiplier`为浮点数。

- `k_process_pin_cap : multiplier ;`
- `k_process_wire_cap : multiplier ;`
- `k_temp_pin_cap : multiplier ;`
- `k_temp_wire_cap : multiplier ;`
- `k_volt_pin_cap : multiplier ;`
- `k_volt_wire_cap : multiplier ;`

## 与非线性延迟模型相关的比例因子
- `k_process_cell_rise`
- `k_temp_cell_rise`
- `k_volt_cell_rise`
- `k_process_cell_fall`
- `k_temp_cell_fall`
- `k_volt_cell_fall`
- `k_process_cell_rise_propagation`
- `k_temp_cell_rise_propagation`
- `k_volt_cell_rise_propagation`
- `k_process_cell_fall_propagation`
- `k_temp_cell_fall_propagation`
- `k_volt_cell_fall_propagation`
- `k_process_cell_rise_transition`
- `k_temp_cell_rise_transition`
- `k_volt_cell_rise_transition`
- `k_process_cell_fall_transition`
- `k_temp_cell_fall_transition`
- `k_volt_cell_fall_transition`


