`ifndef __SANITY2_SV__
`define __SANITY2_SV__

class sanity2 extends jelly_bean_base_test;
   `uvm_component_utils( sanity2 )

   function new( string name, uvm_component parent );
      super.new( name, parent );
   endfunction: new

   task main_phase( uvm_phase phase );
      uvm_reg_hw_reset_seq reg_hw_reset_seq;

      phase.raise_objection( .obj( this ) );
      reg_hw_reset_seq = uvm_reg_hw_reset_seq::type_id::create( .name( "reg_hw_reset_seq" ) );
      reg_hw_reset_seq.model = jb_reg_block;
      reg_hw_reset_seq.start( .sequencer( jb_env.jb_agent.jb_seqr ) );
      
      phase.drop_objection( .obj( this ) );
   endtask: main_phase
endclass: sanity2

`endif
